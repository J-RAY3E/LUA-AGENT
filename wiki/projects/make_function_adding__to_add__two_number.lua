function addnumbers(num1, num2)
    luaL_addi32(B, num1, num2, 0, 0)
    text = "Number"
    luaL_gettext(B, text)
    luaL_settext(text, text)
    luaL_error(B)
end