#########

filename = input("Enter the filename: ")

with open(filename) as file:
    headings = file.readline()

    teams_list = []
    wins_list = []
    last_win_list = []
    win_percentages_list = []


    for line in file:
        team, wins, last_final_won, runners_up, last_final_lost, total_final_appearances = line.strip().split(",")
        
        teams_list.append(team)
        wins_list.append(int(wins))
        if last_final_won.isnumeric():
            last_win_list.append(int(last_final_won))
        else:
            last_win_list.append(0)

        win_percentages_list.append(int(100 * int(wins) / int(total_final_appearances)))

#######


# Split the line into components
for line in data_file.readlines():
    team, wins, last_win, _, _, win_ratio = line.split(",")

results[team] = (int(wins), last_win, int(win_ratio.strip("%\n")))

# Total and average

print(f"Number of Counties: {len(results)}")
total_final = sum([value[0] for value in results.values()])
print(f"Total number of All-Irealdn finals: {total_final}")
print(f"Average number of wins per county: {total_finals/len(reults):.1f}")

# Current champions
champions = max(results, key=lambda k: int(results[k][1]) if results[k][1].isdigit() else 0)
print(f"Champions in {results[champions][1]: {champions}")
