#metoda str.format()
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:} głosów na TAK {:2.2%}'.format(yes_votes, percentage))
