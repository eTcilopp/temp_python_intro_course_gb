from pathlib import Path


def rename_files(
    directory: str,
    new_name: str,
    sequence_number_length: int,
    inbound_extension: str,
    outbound_extension: str,
    old_name_slice: list[int] = [None, None]
) -> dict[bool, str]:

    if not Path(directory).is_dir():
        return {"result": False, "message": "Directory does not exist."}

    sequence_number = 1
    error_count = 0
    for file in Path(directory).iterdir():
        if file.suffix == inbound_extension:
            new_name = (
                f'{file.stem[old_name_slice[0]:old_name_slice[1]]}{new_name}-'
                f'{str(sequence_number).zfill(sequence_number_length)}'
                f'{outbound_extension}'
            )
            try:
                file.rename(Path(directory) / new_name)
                sequence_number += 1
            except Exception:
                error_count += 1
    return {"result": True, "message": f"Renamed {sequence_number} files {'with' if error_count else 'without'} {error_count} errors."}
