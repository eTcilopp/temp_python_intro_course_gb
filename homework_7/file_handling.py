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
                pass
    return {"result": True, "message": f"Renamed {sequence_number} files"}


rename_files(r'W:\DATA\STUDY\GB2\31. Погружение в Python\temp_python_intro_course_gb\dive_into_python\homework_7_test', 'eight_queens_', 2, '.txt', '.txt', [0, 2])