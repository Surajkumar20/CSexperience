# This program calculates GPA from a text file
from os import stat


def main():
    printer(gpa_engine(reader('GPA.txt')))

''' This function formats output to be printed'''
def printer(stat_):
    print("Your GPA is {:0.2f}!".format(stat_))

'''This function reads in the data from the text file'''
def reader(file_name):
    output = []
    f = open(file_name, 'r')
    i = 0 # Counter to check if it's a white line or not
    while True:
        contents = f.readline().split()
        if i % 2 == 0:
            # This is to get rid of while lines
            if not contents:
                break
            
            # Adding the data into the output list
            output.append(converter(contents))
        i += 1

    return(output)

'''This function returns the GPA points'''
def gpa_engine(stats):
    ls_gds   = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'P', 'NP', 'W', 'WF']
    cdt_hr_pts = [ 4,    4,   3.7,  3.3,  3.0, 2.7,  2.3,  2.0, 1.7,  1.3,  1.0, 0.7,  0.3, 0,   0,    0,   0]
    credits  = 0
    q_points = 0
    
    for element in stats:
        if (element[3] == 'P') or (element[3] == 'NP') or (element[3] == 'W') or (element[3] == 'WF'):
            credits += 0
            q_points += 0 * cdt_hr_pts[ls_gds.index(element[3])]
        else:
            credits += element[2]
            q_points += element[2] * cdt_hr_pts[ls_gds.index(element[3])]
    
    return(q_points / credits)

'''This function converts string list into the numbers'''
def converter(str_ls):
    return([str_ls[0], str_ls[1], eval(str_ls[2]), str_ls[3]])

if __name__ == "__main__":
    main()
