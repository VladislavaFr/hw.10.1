from src.processing import filter_by_state
from src.processing import sort_by_date
from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import get_date
from src.widget import mask_account_card

card_number = "7000792289606361"
masked_card_number = get_mask_card_number(card_number)
print(masked_card_number)

account_number = "73654108430135874305"
masked_account_number = get_mask_account(account_number)
print(masked_account_number)

card1 = "Maestro 1596837868705199"
mask_card1 = mask_account_card(card1)
card2 = "Visa Classic 6831982476737658"
mask_card2 = mask_account_card(card2)

acc1 = "Maestro 1596837868705199"
mask_acc1 = mask_account_card(acc1)
acc2 = "Visa Classic 6831982476737658"
mask_acc2 = mask_account_card(acc2)

date1 = "2024-03-11T02:26:18.671407"
sort_date = get_date(date1)



executed_data = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
canceled_data = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                state='CANCELED')

sorted_data = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
