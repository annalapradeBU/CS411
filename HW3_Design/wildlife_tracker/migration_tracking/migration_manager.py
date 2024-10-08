# he Migration Management module allows users to create and manage migrations 
# along predefined paths between habitats, including scheduling, viewing, 
# and canceling migration events. Users can also manage Migration Paths, 
# specifying starting and ending habitats, species involved, and migration duration


from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class MigrationManager:
    
    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass

    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def get_migration_path_details(path_id) -> dict:
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass

    def cancel_migration(migration_id: int) -> None:
        pass

    def get_migration_paths() -> list[MigrationPath]:
        pass
    
    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
     pass
    

    pass
