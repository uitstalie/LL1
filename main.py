from LL1 import LL1Method
bdsj = LL1Method()
bdsj.create_expression_list("234.txt","1")
bdsj.look()    
bdsj.create_epsilon_table()
bdsj.create_vt_first_table()
bdsj.create_right_first_table()
bdsj.merge()
bdsj.create_follow_table()
bdsj.create_select_table()
ans = bdsj.LL1_judge()
print(ans)
if ans[0]== True:
    bdsj.create_predict_tablle()
    print(bdsj.predict("i+i*i"))