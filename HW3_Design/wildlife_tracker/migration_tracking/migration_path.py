# Users can also manage Migration Paths, specifying starting and ending habitats, 
# species involved, and migration duration. 



from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat


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

    pass