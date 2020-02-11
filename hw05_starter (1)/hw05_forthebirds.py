# ----------------------------------------------------------
# --------              HW 5: Part 3               ---------
# ----------------------------------------------------------

############################################################
######## Do not modify any of the code in this file ########
############################################################

############################################################
# You can run this file to start with and see that the     #
# program does not work correctly.  This is because the    #
# format of the data is not what the program expects. You  #
# should write functions as described in the homework      #
# assignment in the file hw05_reformat.  Once you do, this #
# program will work becuase your hw05_reformat functions   #
# will reformat the data to a format that this program     #
# understands.                                             #
############################################################

import hw05_reformat as reformat

def get_data_from_file(filename):
    data_file = open(filename)
    data = data_file.readlines()
    data_file.close()
    return data

def convert_to_int(alist):

    new_list = []

    for i in range(len(alist)):
        new_list.append(int(alist[i]))

    return new_list


def organize_data(data_list):

    data_dictionary = {}

    for item in data_list:
        participant_data = item.strip('\n').split(',')
        key = participant_data[0]
        values = participant_data[1:]

        #make a dictionary whose keys are bird type, and values lists of data
        if key not in data_dictionary:
            data_dictionary[key] = convert_to_int(values)
        else:
            data_dictionary[key] = data_dictionary[key] + convert_to_int(values)

    return data_dictionary

def analyze_data(all_bird_data):

    all_bird_info = {}

    # make a dictionary with bird type as key
    # value is another dictionary with keys: data_points, occasions, ave group size
    #          max group size, min group size, total_sightings
    bird_types = all_bird_data.keys()
    for bird_type in bird_types:
        bird_info = {}
        bird_data = all_bird_data[bird_type]
        bird_info['reports'] = bird_data
        bird_info['occasions'] = len(bird_data)
        bird_info['total_count'] = sum(bird_data)
        if bird_data != []:
            bird_info['max_group_size'] = max(bird_data)
            bird_info['min_group_size'] = min(bird_data)
            bird_info['ave_group_size'] = int(bird_info['total_count']/bird_info['occasions'])
        else:
            bird_info['max_group_size'] = 0
            bird_info['min_group_size'] = 0
            bird_info['ave_group_size'] = 0
        all_bird_info[bird_type] = bird_info

    return all_bird_info

def find_max_length(strings):
    maxlen = 0
    for string in strings:
        if len(string) > maxlen:
            maxlen = len(string)
    return maxlen

def num_tabs(string, maxstring):
    tabs = (maxstring-len(string))//5 + 1
    return tabs

def display_group_data(bird_data):

    all_species = bird_data.keys()
    max_len = find_max_length(all_species)

    #print Heading
    print()
    print("\t\t Bird Group Size Data by Species")
    print()
    print("Species\t\t\t", "Groups\t", " Max\t", " Min\t", "Average")

    for species in all_species:
        print(species, end='\t'*num_tabs(species,max_len))
        info_types = bird_data[species].keys()
        for info_type in info_types:
            if info_type != 'reports' and info_type != 'total_count':
                print(" ",bird_data[species][info_type], end='\t')
        print('')



def main():
    bird_data = get_data_from_file('sample_bird_data.txt')
    if len(bird_data) == 1:
        bird_data = reformat.reformat_data(bird_data[0])
    bird_data = organize_data(bird_data)
    bird_data = analyze_data(bird_data)
    display_group_data(bird_data)


if __name__ == '__main__':
    main()
