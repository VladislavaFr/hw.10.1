from src.processing import filter_by_state
from src.processing import sort_by_date

executed_data = filter_by_state(data)
canceled_data = filter_by_state(data, state='CANCELED')
sorted_data = sort_by_date(data)