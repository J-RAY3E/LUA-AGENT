#!/usr/bin/env python3
"""
Test Suite for Lua Coding Agent - MWS Octapi Edition.
Based on Public Selection PDF (Публичная выборка LocalScript.pdf).
Features:
- Context Injection: Injects exact JSON structures from the PDF into prompts.
- Accurate Logic Checks: Validates against expected patterns in the PDF.
- Windows Compatible: Uses 'where' instead of 'which'.
- Safe File Naming: Sanitizes filenames to avoid OS errors.
"""
import sys
import os
import subprocess
import time
import datetime
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from agents.coder import generate_code, save_code
    from agents.validator import validate_and_reconstruct_lua
    HAS_AGENT = True
except ImportError as e:
    print(f"[!] CRITICAL ERROR: Could not import agent modules.")
    print(f"    Make sure 'agents/' folder exists with coder.py and validator.py.")
    print(f"    Error details: {e}")
    HAS_AGENT = False
    sys.exit(1)

# ==============================================================================
# DATABASE DATA DUMMY (Dari Dokumen PDF: Публичная выборка LocalScript.pdf)
# ==============================================================================
TEST_DATA_CONTEXT = {
    "Last Array Element": """
DATA CONTEXT EXAMPLE (wf.vars.emails):
{
  "wf": {
    "vars": {
      "emails": [
        "user1@example.com", 
        "user2@example.com", 
        "user3@example.com"
      ]
    }
  }
}
""",
    "Increment Counter": """
DATA CONTEXT EXAMPLE (wf.vars.try_count_n):
{
  "wf": {
    "vars": {
      "try_count_n": 3
    }
  }
}
""",
    "Clean Variables (REST Body)": """
DATA CONTEXT EXAMPLE (wf.vars.RESTbody.result):
{
  "wf": {
    "vars": {
      "RESTbody": {
        "result": [
          {
            "ID": 123, 
            "ENTITY_ID": 456, 
            "CALL": "example_call_1", 
            "OTHER_KEY_1": "value1", 
            "OTHER_KEY_2": "value2"
          },
          {
            "ID": 789, 
            "ENTITY_ID": 101, 
            "CALL": "example_call_2", 
            "EXTRA_KEY_1": "value3", 
            "EXTRA_KEY_2": "value4"
          }
        ]
      }
    }
  }
}
""",
    "ISO 8601 Conversion": """
DATA CONTEXT EXAMPLE (wf.vars.json.IDOC.ZCDF_HEAD - Lengkap sesuai PDF):
{
  "wf": {
    "vars": {
      "json": {
        "IDOC": {
          "ZCDF_HEAD": {
            "DELIVERY": "123456789",
            "SUBJECT": "Order Confirmation",
            "DATUM": "20231015",
            "TIME": "153000",
            "STATUS": "Confirmed",
            "ROUTE": "Route 66",
            "ROUTE_TXT": "Main Distribution Route",
            "ZCDF_PACKAGES": [
              {
                "id": "PKG001",
                "number": "EXIDV001",
                "weight": "10",
                "volume": "50",
                "length": "100",
                "width": "50",
                "height": "30",
                "items": [
                  { "sku": "SKU001", "externalId": "MAT001", "quantity": "5", "weight": "2" },
                  { "sku": "SKU002", "externalId": "MAT002", "quantity": "3", "weight": "1" }
                ]
              },
              {
                "id": "PKG002",
                "number": "EXIDV002",
                "weight": "20",
                "volume": "60",
                "length": "120",
                "width": "60",
                "height": "40",
                "items": [
                  { "sku": "SKU003", "externalId": "MAT003", "quantity": "10", "weight": "2" }
                ]
              }
            ]
          }
        }
      }
    }
  }
}
""",
    "Type Check & Normalize Items": """
DATA CONTEXT EXAMPLE (wf.vars.json.IDOC.ZCDF_HEAD.ZCDF_PACKAGES - Lengkap sesuai PDF):
{
  "wf": {
    "vars": {
      "json": {
        "IDOC": {
          "ZCDF_HEAD": {
            "ZCDF_PACKAGES": [
              {
                "id": "PKG001",
                "number": "EXIDV001",
                "weight": "10",
                "volume": "50",
                "length": "100",
                "width": "50",
                "height": "30",
                "items": [
                  { "sku": "SKU001", "externalId": "MAT001", "quantity": "5", "weight": "2" },
                  { "sku": "SKU002", "externalId": "MAT002", "quantity": "3", "weight": "1" }
                ]
              },
              {
                "id": "PKG002",
                "number": "EXIDV002",
                "weight": "20",
                "volume": "60",
                "length": "120",
                "width": "60",
                "height": "40",
                "items": { "sku": "SKU003" } 
              }
            ]
          }
        }
      }
    }
  }
}
""",
    "Filter Array (Discount/Markdown)": """
DATA CONTEXT EXAMPLE (wf.vars.parsedCsv):
{
  "wf": {
    "vars": {
      "parsedCsv": [
        {"SKU": "A001", "Discount": "10%", "Markdown": ""},
        {"SKU": "A002", "Discount": "", "Markdown": "5%"},
        {"SKU": "A003", "Discount": null, "Markdown": null},
        {"SKU": "A004", "Discount": "", "Markdown": ""}
      ]
    }
  }
}
""",
    "Code Extension (Square)": """
DATA CONTEXT EXAMPLE:
No specific structure required. Just calculate square of 5.
""",
    "Unix Epoch Conversion": """
DATA CONTEXT EXAMPLE (wf.initVariables.recallTime):
{
  "wf": {
    "initVariables": {
      "recallTime": "2023-10-15T15:30:00+00:00"
    }
  }
}
"""
}

# ==============================================================================
# TEST CASES DEFINITION (Sesuai PDF)
# ==============================================================================
TEST_CASES = [
    {
        "name": "Last Array Element",
        "request": "Из полученного списка email получи последний.",
        # Expected: return wf.vars.emails[#wf.vars.emails]
        "check_func": lambda c: ("return" in c and "wf.vars.emails[#wf.vars.emails]" in c)
    },
    {
        "name": "Increment Counter",
        "request": "Увеличивай значение переменной try_count_n на каждой итерации",
        # Expected: return wf.vars.try_count_n + 1
        "check_func": lambda c: ("return" in c and "wf.vars.try_count_n + 1" in c)
    },
    {
        "name": "Clean Variables (REST Body)",
        "request": "Для полученных данных из предыдущего REST запроса очисти значения переменных ID, ENTITY_ID, CALL",
        # Expected: Nested loops with pairs, checking key != ID/ENTITY_ID/CALL, setting to nil
        "check_func": lambda c: (
            "pairs(result)" in c and 
            "pairs(filteredEntry)" in c and 
            "key~=\"ID\"" in c and 
            "key~=\"ENTITY_ID\"" in c and 
            "key~=\"CALL\"" in c and 
            "filteredEntry[key]= nil" in c
        )
    },
    {
        "name": "ISO 8601 Conversion",
        "request": "Преобразуй время из формата 'YYYYMMDD' и 'HHMMSS' в строку в формате ISO 8601 с использованием Lua.",
        # Expected: safe_sub function, string.format('%s-%s-%sT%s:%s:%s.00000Z', ...)
        "check_func": lambda c: (
            "function safe_sub" in c and 
            "string.sub(str, start, math.min(finish,#str))" in c and
            "string.format" in c and 
            "'%s-%s-%sT%s:%s:%s.00000Z'" in c and
            "wf.vars.json.IDOC.ZCDF_HEAD.DATUM" in c and
            "wf.vars.json.IDOC.ZCDF_HEAD.TIME" in c
        )
    },
    {
        "name": "Type Check & Normalize Items",
        "request": "Как преобразовать структуру данных так, чтобы все элементы items в ZCDF_PACKAGES всегда были представлены в виде массивов, даже если они изначально не являются массивами",
        # Expected: Function ensureArray using type(k) and math.floor(k), then ensureAllItemsAreArrays
        "check_func": lambda c: (
            "function ensureArray(t)" in c and 
            "type(k)~=\"number\" or math.floor(k)~= k" in c and
            "function ensureAllItemsAreArrays(objectsArray)" in c and
            "obj.items= ensureArray(obj.items)" in c
        )
    },
    {
        "name": "Filter Array (Discount/Markdown)",
        "request": "Отфильтруй элементы из массива, чтобы включить только те, у которых есть значения в полях Discount или Markdown.",
        # Expected: _utils.array.new(), check (item.Discount~="" and item.Discount~= nil) or ...
        "check_func": lambda c: (
            "_utils.array.new()" in c and 
            "wf.vars.parsedCsv" in c and 
            "(item.Discount~=\"\" and item.Discount~= nil)" in c and
            "(item.Markdown~=\"\" and item.Markdown~= nil)" in c and
            "table.insert(result, item)" in c
        )
    },
    {
        "name": "Code Extension (Square)",
        "request": "Добавь переменную с квадратом числа",
        # Expected: local n = tonumber('5'); return n * n
        "check_func": lambda c: (
            "local n = tonumber('5')" in c and 
            "return n * n" in c
        )
    },
    {
        "name": "Unix Epoch Conversion",
        "request": "Конвертируй время в переменной recallTime в unix-формат.",
        # Expected: Complex parsing logic with is_leap_year, days_since_epoch, parse_iso8601_to_epoch
        "check_func": lambda c: (
            "wf.initVariables.recallTime" in c and 
            "is_leap_year(year)" in c and 
            "days_since_epoch(year, month, day)" in c and
            "parse_iso8601_to_epoch(iso_str)" in c
        )
    }
]

def run_test(test_case):
    """
    Execute a single test case.
    Injects context data if available, then generates and validates code.
    Returns (passed_bool, generated_code_str).
    """
    print(f"\n{'='*60}")
    print(f"RUNNING: {test_case['name']}")
    print(f"   Request: \"{test_case['request']}\"")
    
    # --- LOGIKA INJEKSI DATA DUMMY ---
    final_request = test_case['request']
    context_data = TEST_DATA_CONTEXT.get(test_case['name'])
    
    if context_data and context_data.strip():
        # Gabungkan request dengan konteks data agar LLM tahu struktur datanya
        final_request = f"{final_request}\n\nREFERENCE DATA STRUCTURE:\n{context_data}"
        print(f"   [CONTEXT INJECTED] Data structure provided for this test.")
    else:
        print(f"   [INFO] No specific data context found. Using general knowledge.")

    generated_code_snippet = "" 

    try:
        start_time = time.time()

        # Generate code using the enriched request
        code = generate_code(final_request)
        generated_code_snippet = code if code else "-- No code generated"

        duration = time.time() - start_time

        if not code or code.startswith("--"):
            print(f"FAILED: Agent did not produce valid code.")
            print(f"   Output: {code[:100] if code else 'None'}...")
            return False, generated_code_snippet

        print(f"Execution Time: {duration:.2f}s")
        print(f"Preview:\n{code[:300]}...\n")

        # Validate Syntax via AST
        print("Validating Syntax (AST)...")
        cleaned_code = validate_and_reconstruct_lua(code)
        
        if cleaned_code:
            generated_code_snippet = cleaned_code

        if not cleaned_code:
            print(f"FAILED: Generated code has invalid Lua syntax.")
            print(f"   Raw code was: {code[:200]}")
            return False, generated_code_snippet

        print("Syntax is VALID!")

        # Verify Logic against expected patterns
        print("Verifying Logic...")
        if test_case['check_func'](cleaned_code):
            print("Logic matches expectations (PASS).")
            passed_logic = True
        else:
            print("WARNING: Logic might not match expectations perfectly.")
            print(f"   (Check output snippet: {cleaned_code[:300]})")
            passed_logic = False

        # --- SANITASI NAMA FILE (Windows Safety) ---
        safe_name_base = f"test_{test_case['name'].lower().replace(' ', '_')}"
        # Hapus karakter terlarang di Windows: < > : " / \ | ? *
        safe_name_clean = re.sub(r'[<>:"/\\|?*]', '_', safe_name_base)
        safe_name = f"{safe_name_clean}.lua"
        
        save_code(cleaned_code, safe_name)
        print(f"Saved individual file to: projects/{safe_name}")

        # --- EKSEKUSI LUA (Jika tersedia) ---
        lua_binary = None
        candidates = ["lua", "lua5.4", "lua5.3", "lua.exe"]
        
        # Deteksi OS: Windows menggunakan 'where', Linux/Mac menggunakan 'which'
        is_windows = os.name == 'nt'
        search_cmd = "where" if is_windows else "which"

        for candidate in candidates:
            result_check = subprocess.run([search_cmd, candidate], capture_output=True, text=True)
            if result_check.returncode == 0:
                lua_binary = candidate
                break

        if lua_binary:
            print(f"Running execution test with '{lua_binary}'...")
            result = subprocess.run([lua_binary, safe_name], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("Code executed successfully (Standalone)!")
                if result.stdout:
                    print(f"   Output: {result.stdout.strip()}")
            else:
                stderr = result.stderr.lower()
                if "syntax" in stderr or "unexpected symbol" in stderr:
                    print(f"Runtime Syntax Error: {result.stderr}")
                    passed_logic = False
                else:
                    # Biasanya error karena variabel wf.vars tidak ada di environment lokal
                    print(f"Expected Runtime Context Error (wf vars missing): {result.stderr[:80]}...")
        else:
            print("Skipped: Lua interpreter not found in PATH.")

        return passed_logic, generated_code_snippet

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False, generated_code_snippet

def save_results_to_txt(results_log):
    """Saves the test results summary to a text file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_results_{timestamp}.txt"
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("="*60 + "\n")
            f.write("LUA CODING AGENT TEST RESULTS\n")
            f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            passed_count = 0
            failed_count = 0
            
            for res in results_log:
                status_str = "PASS" if res['status'] else "FAIL"
                if res['status']:
                    passed_count += 1
                else:
                    failed_count += 1
                    
                f.write(f"TEST: {res['name']}\n")
                f.write(f"STATUS: {status_str}\n")
                f.write("-" * 40 + "\n")
                f.write("Generated Code Snippet:\n")
                f.write(res['code'][:1000]) 
                if len(res['code']) > 1000:
                    f.write("\n... (truncated)")
                f.write("\n\n" + "="*60 + "\n\n")
            
            f.write("SUMMARY\n")
            f.write(f"Total: {len(results_log)}\n")
            f.write(f"Passed: {passed_count}\n")
            f.write(f"Failed: {failed_count}\n")
            
        print(f"\n[INFO] Full results saved to: {filename}")
        
    except Exception as e:
        print(f"\n[ERROR] Could not save results to txt: {e}")

def main():
    if not HAS_AGENT:
        return

    print("\nINITIALIZING LUA CODING AGENT TEST SUITE (MWS OCTAPI EDITION)\n")

    passed = 0
    failed = 0
    results_log = [] 

    for test in TEST_CASES:
        success, code_snippet = run_test(test)
        
        results_log.append({
            "name": test['name'],
            "status": success,
            "code": code_snippet
        })

        if success:
            passed += 1
        else:
            failed += 1

    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Total Tests: {len(TEST_CASES)}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")

    save_results_to_txt(results_log)

    if failed == 0:
        print("\nALL TESTS PASSED! The Agent is ready for MWS Octapi tasks.")
    else:
        print(f"\n{failed} test(s) failed. Review logs above or the generated .txt file.")
        print("Note: Some failures may be due to LLM output variation vs strict pattern matching.")

if __name__ == "__main__":
    main()