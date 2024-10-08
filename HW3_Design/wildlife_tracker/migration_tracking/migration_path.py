# Users can also manage Migration Paths, specifying starting and ending habitats, 
# species involved, and migration duration. 



from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration


class MigrationPath:
    def __init__(self,
                path_id: int,
                species: str,
                destination: Habitat,
                 start_location: Habitat,
                duration: Optional[int] = None): 
        self.path_id = path_id
        self.species = species
        self.destination = destination
        self.start_location = start_location
        self.duration = duration

    def get_migration_path_details(self, path_id) -> dict:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass

    

    pass