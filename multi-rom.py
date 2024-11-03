import subprocess

def randomize_rom(rom_path, output_path, rnqs_file):
    """
    Randomizes a Pokémon ROM using UPRandomizer with a specified .rnqs file.

    Args:
        rom_path (str): Path to the input ROM.
        output_path (str): Path to the output ROM.
        rnqs_file (str): Path to the .rnqs file with settings.
    """

    # Construct the UPRandomizer command-line arguments
    args = [
        "UPRandomizer-172-win/randomizer.exe",
        "-i", rom_path,
        "-o", output_path,
        "-q", rnqs_file
    ]

    # Run the UPRandomizer process
    subprocess.run(args)

# Example usage:
rom_path = "original_rom.gba"
rnqs_file = "balanced.rnqs"

for i in range(3):
    output_path = f"randomized_rom_{i}.gba"
    randomize_rom(rom_path, output_path, rnqs_file)