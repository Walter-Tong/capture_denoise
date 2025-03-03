# Denoise Capture Application

## Overview
`denoise_capture.exe` is a simple application for capturing video with various denoising filters. The application allows you to configure video capture settings and denoising algorithms through a configuration file (`setting.txt`).

## Features
- Capture video with customizable resolution, frame rate, and codec.
- Select from multiple capture backends.
- Apply various denoising algorithms including bilateral, fastNlMeans, Gaussian, median, edge-preserving, and detail enhancement filters.
- Easily configurable settings via `setting.txt`.

## Configuration
The application uses a configuration file named `setting.txt` to load settings for video capture and denoising filters. You can modify this file to change the settings according to your needs.

## Usage
1. Download the latest release of `denoise_capture.exe` from the GitHub releases page.
2. Place `denoise_capture.exe` and `setting.txt` in the same directory.
3. Modify `setting.txt` to configure the video capture and denoising settings as needed.
4. Run `denoise_capture.exe`.
5. Press **`Q`** to exit the application.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please read the `CONTRIBUTING` guidelines before submitting a pull request.

## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.