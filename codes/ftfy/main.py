# pip install ftfy

from ftfy import fix_text
print(fix_text('âœ” No problems'))  
# 输出: '✔ No problems'

print(fix_text('The Mona Lisa doesnÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢t have eyebrows.'))
# 输出: "The Mona Lisa doesn't have eyebrows."