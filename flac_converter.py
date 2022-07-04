import sys 
import os
import shutil
import ffmpeg
from typing import List
from pathlib import Path

class FlacConverter():
    def __init__(self, input_dir: str, output_dir: str) -> None:
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.whitelist = ['.mp3', '.wav', '.aiff']
        self.target = '.flac'
        
        self.input_files = self._get_all_flac_files(self.input_dir)
    
    def _skip_conversion(self, filename: str, folder: str) -> None:
        input_path = Path(folder) / Path(filename)
        if not (self.output_dir / Path(filename)).exists():
            shutil.copy2(input_path, self.output_dir)
            print(filename, 'copied directly to', self.output_dir)

    def _check_filetype(self, filename: str, folder: str, list_of_flacs: List[Path]) -> None:
        if Path(filename).suffix in self.whitelist:
            self._skip_conversion(filename, folder)
        elif Path(filename).suffix == self.target:
            list_of_flacs.append(Path(folder) / Path(filename))
    
    def _get_all_flac_files(self, input_dir: Path) -> List[Path]:
        flac_list = []
        for folder, subfolders, filenames in os.walk(input_dir):
            for filename in filenames:
                self._check_filetype(filename, folder, flac_list)
        return flac_list
    
    def _create_output_filename(self, input_filename: Path, output_format: Path) -> Path:
        output_file = self.output_dir / input_filename.with_suffix(output_format).name
        return output_file
    
    def convert_files(self, output_format: str) -> None:
        output_form = output_format.split('.')[1]
        for file in self.input_files:
            file_out = self._create_output_filename(file, output_format)
            if not file_out.exists():
                print("Writing: ", file.name, 'to: ', file_out)
                ffmpeg.input(file).output(str(file_out), format=output_form, write_id3v2=1).run_async()
            else: 
                print(file.name, "already exists in output directory")
            
if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    output_format = sys.argv[3]
    FlacConverter(input_dir, output_dir).convert_files(output_format)