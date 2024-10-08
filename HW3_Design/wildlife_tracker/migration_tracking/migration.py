class Migration:
    def __init__(self,
                 current_location: str,
                 start_date: str,
                 migration_id: int, 
                 current_date: str,
                 status: str = "Scheduled"): 
        self.current_location = current_location
        self.start_date = start_date
        self.migration_id = migration_id
        self.current_date = current_date
        self.status = status
       
        

    pass