def calculate_number_of_pages(total_records, take):
    if total_records == 0:
        return 0 
    
    pages, remainder = divmod(total_records, take)
    if remainder > 0:
        pages += 1
        
    return pages