from typing import Any
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    def __init__(self,
                 current_location: str,
                 start_date: str,
                 migration_id: int, 
                 current_date: str,
                 migration_path: MigrationPath,
                 status: str = "Scheduled"): 
        self.current_location = current_location
        self.start_date = start_date
        self.migration_id = migration_id
        self.current_date = current_date
        self.migration_path= migration_path
        self.status = status
       
    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        pass   

    def get_migration_details(self, migration_id: int) -> dict[str, Any]:
        pass

    


    pass