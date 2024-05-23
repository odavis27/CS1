import timeit

the_code = '''
import random

options = [ [['A Plane ',7],['A Car ',2],['Roller Skates ',5],['A zipline ',1],['A Rocket ',6],['An unintentional submarine ',3],['An intentional submarine ',4]],[['Made of Wood ',3],['Made of Duct Tape ',2],['Made Mostly of hot glue ',5],['Made of LEGOs ',1],['Made of Garbage and Recycling ',6],['Made of Cylinders ',4],['Made of Stuff You Find Outside ',7]],[['Powered by the Wind.',6],['Powered by Water.',3],['That is Partially Edible.',1],['With Rockets Attached to it.',7],['Covered in Hot Glue.',2],['That is Very Dangerous.',5],['That Attacks My Brother.',4]]]

user_input = 5
print('========================================')
for i in range(user_input): 
    choices = [random.choice(i) for i in options] 
    print(choices[0][0]+choices[1][0]+choices[2][0])
'''

print(timeit.timeit(stmt=the_code,number=100000))