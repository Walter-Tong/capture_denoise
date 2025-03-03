import cv2
import numpy as np
import os

def load_settings(filename):
    """
    Load settings from a text file with key=value pairs.
    Ignores empty lines and comments (lines starting with '#').
    """
    settings = {}
    if not os.path.exists(filename):
        print(f"Settings file '{filename}' not found. Using defaults.")
        return settings

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if '=' in line:
                key, value = line.split("=", 1)
                settings[key.strip()] = value.strip()
    return settings

def save_settings(settings, filename):
    """
    Save/update settings to file. If missing, defaults are added.
    """
    with open(filename, 'w') as f:
        f.write("# Settings for video capture, backend and denoising filters\n")
        # Camera settings
        f.write(f"width={settings.get('width', 1920)}\n")
        f.write(f"height={settings.get('height', 1080)}\n")
        f.write(f"fps={settings.get('fps', 60)}\n")
        f.write(f"fourcc={settings.get('fourcc', 'MJPG')}\n\n")
        
        # Capture backend option
        f.write("# Capture backend options: CAP_ANY, CAP_DSHOW, CAP_V4L2, CAP_MSMF\n")
        f.write(f"capture_backend={settings.get('capture_backend', 'CAP_DSHOW')}\n\n")
        
        # Denoising algorithm
        f.write("# Denoising algorithm options:\n")
        f.write("# Available options: none, bilateral, fastnlmeans, fastnlmeanscolored, gaussian, median, edgepreserving, detailenhance\n")
        f.write("# It is recommend to use bilateral/gaussian, other filter require too much computation resource\n")
        f.write(f"denoising_algo={settings.get('denoising_algo', 'bilateral')}\n\n")

        # Bilateral filter parameters
        f.write("# Bilateral filter parameters\n")
        f.write(f"bilateral_d={settings.get('bilateral_d', 3)}\n")
        f.write(f"bilateral_sigmaColor={settings.get('bilateral_sigmaColor', 75)}\n")
        f.write(f"bilateral_sigmaSpace={settings.get('bilateral_sigmaSpace', 100)}\n\n")
        
        # fastNlMeansDenoising (grayscale) parameters
        f.write("# fastNlMeansDenoising parameters (for grayscale images)\n")
        f.write(f"fastNlMeans_h={settings.get('fastNlMeans_h', 10)}\n")
        f.write(f"fastNlMeans_templateWindowSize={settings.get('fastNlMeans_templateWindowSize', 7)}\n")
        f.write(f"fastNlMeans_searchWindowSize={settings.get('fastNlMeans_searchWindowSize', 21)}\n\n")
        
        # fastNlMeansDenoisingColored parameters (for color images)
        f.write("# fastNlMeansDenoisingColored parameters (for colored images)\n")
        f.write(f"fastNlMeansColored_h={settings.get('fastNlMeansColored_h', 10)}\n")
        f.write(f"fastNlMeansColored_hColor={settings.get('fastNlMeansColored_hColor', 10)}\n")
        f.write(f"fastNlMeansColored_templateWindowSize={settings.get('fastNlMeansColored_templateWindowSize', 7)}\n")
        f.write(f"fastNlMeansColored_searchWindowSize={settings.get('fastNlMeansColored_searchWindowSize', 21)}\n\n")
        
        # Gaussian blur parameters
        f.write("# Gaussian blur parameters\n")
        f.write(f"gaussian_kernel_width={settings.get('gaussian_kernel_width', 5)}\n")
        f.write(f"gaussian_kernel_height={settings.get('gaussian_kernel_height', 5)}\n")
        f.write(f"gaussian_sigma={settings.get('gaussian_sigma', 1.0)}\n\n")

        # Median filter parameter
        f.write("# Median filter parameter\n")
        f.write(f"median_kernel_size={settings.get('median_kernel_size', 5)}\n\n")
        
        # Edge preserving filter parameters
        f.write("# Edge preserving filter parameters\n")
        f.write(f"edgepreserving_flags={settings.get('edgepreserving_flags', 1)}\n")
        f.write(f"edgepreserving_sigma_s={settings.get('edgepreserving_sigma_s', 60)}\n")
        f.write(f"edgepreserving_sigma_r={settings.get('edgepreserving_sigma_r', 0.4)}\n\n")
        
        # Detail enhance filter parameters
        f.write("# Detail enhance filter parameters\n")
        f.write(f"detailenhance_sigma_s={settings.get('detailenhance_sigma_s', 10)}\n")
        f.write(f"detailenhance_sigma_r={settings.get('detailenhance_sigma_r', 0.15)}\n")

# Main Program

settings_file = "setting.txt"

# Load settings from file
settings = load_settings(settings_file)

# Camera settings
width = int(settings.get("width", 1920))
height = int(settings.get("height", 1080))
fps = int(settings.get("fps", 60))
fourcc_str = settings.get("fourcc", "MJPG")

# Capture backend mapping
capture_backend_str = settings.get("capture_backend", "CAP_DSHOW").upper()
backend_mapping = {
    "CAP_ANY": cv2.CAP_ANY,
    "CAP_DSHOW": cv2.CAP_DSHOW,
    "CAP_V4L2": cv2.CAP_V4L2,
    "CAP_MSMF": cv2.CAP_MSMF,
}
capture_backend = backend_mapping.get(capture_backend_str, cv2.CAP_DSHOW)

# Denoising algorithm selection
denoising_algo = settings.get("denoising_algo", "bilateral").lower()

# Bilateral filter parameters
bilateral_d = int(settings.get("bilateral_d", 3))
bilateral_sigmaColor = float(settings.get("bilateral_sigmaColor", 75))
bilateral_sigmaSpace = float(settings.get("bilateral_sigmaSpace", 100))

# fastNlMeansDenoising (grayscale) parameters
fastNlMeans_h = int(settings.get("fastNlMeans_h", 10))
fastNlMeans_templateWindowSize = int(settings.get("fastNlMeans_templateWindowSize", 7))
fastNlMeans_searchWindowSize = int(settings.get("fastNlMeans_searchWindowSize", 21))

# fastNlMeansDenoisingColored parameters (colored images)
fastNlMeansColored_h = int(settings.get("fastNlMeansColored_h", 10))
fastNlMeansColored_hColor = int(settings.get("fastNlMeansColored_hColor", 10))
fastNlMeansColored_templateWindowSize = int(settings.get("fastNlMeansColored_templateWindowSize", 7))
fastNlMeansColored_searchWindowSize = int(settings.get("fastNlMeansColored_searchWindowSize", 21))

# Gaussian blur parameters
gaussian_kernel_width = int(settings.get("gaussian_kernel_width", 5))
gaussian_kernel_height = int(settings.get("gaussian_kernel_height", 5))
gaussian_sigma = float(settings.get("gaussian_sigma", 1.0))

# Median filter parameter
median_kernel_size = int(settings.get("median_kernel_size", 5))

# Edge preserving filter parameters
edgepreserving_flags = int(settings.get("edgepreserving_flags", 1))
edgepreserving_sigma_s = float(settings.get("edgepreserving_sigma_s", 60))
edgepreserving_sigma_r = float(settings.get("edgepreserving_sigma_r", 0.4))

# Detail enhance filter parameters
detailenhance_sigma_s = float(settings.get("detailenhance_sigma_s", 10))
detailenhance_sigma_r = float(settings.get("detailenhance_sigma_r", 0.15))

# Save the settings to ensure the file contains all keys
save_settings(settings, settings_file)

# Initialize video capture
cap = cv2.VideoCapture(0, capture_backend)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, fps)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*fourcc_str))

print("Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    if denoising_algo == "none":
        filtered_frame = frame
    elif denoising_algo == "bilateral":
        filtered_frame = cv2.bilateralFilter(frame, bilateral_d, bilateral_sigmaColor, bilateral_sigmaSpace)
    elif denoising_algo == "fastnlmeans":
        # Convert to grayscale, apply denoising, then convert back to BGR for display
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        denoised_gray = cv2.fastNlMeansDenoising(
            gray,
            h=fastNlMeans_h,
            templateWindowSize=fastNlMeans_templateWindowSize,
            searchWindowSize=fastNlMeans_searchWindowSize
        )
        filtered_frame = cv2.cvtColor(denoised_gray, cv2.COLOR_GRAY2BGR)
    elif denoising_algo == "fastnlmeanscolored":
        filtered_frame = cv2.fastNlMeansDenoisingColored(
            frame,
            None,
            h=fastNlMeansColored_h,
            hColor=fastNlMeansColored_hColor,
            templateWindowSize=fastNlMeansColored_templateWindowSize,
            searchWindowSize=fastNlMeansColored_searchWindowSize
        )
    elif denoising_algo == "gaussian":
        # Ensure the kernel dimensions are odd
        kW = gaussian_kernel_width if gaussian_kernel_width % 2 == 1 else gaussian_kernel_width + 1
        kH = gaussian_kernel_height if gaussian_kernel_height % 2 == 1 else gaussian_kernel_height + 1
        filtered_frame = cv2.GaussianBlur(frame, (kW, kH), gaussian_sigma)
    elif denoising_algo == "median":
        # Ensure kernel is odd
        kernel = median_kernel_size if median_kernel_size % 2 == 1 else median_kernel_size + 1
        filtered_frame = cv2.medianBlur(frame, kernel)
    elif denoising_algo == "edgepreserving":
        filtered_frame = cv2.edgePreservingFilter(frame, flags=edgepreserving_flags, sigma_s=edgepreserving_sigma_s, sigma_r=edgepreserving_sigma_r)
    elif denoising_algo == "detailenhance":
        filtered_frame = cv2.detailEnhance(frame, sigma_s=detailenhance_sigma_s, sigma_r=detailenhance_sigma_r)
    else:
        # Fallback if algorithm is unknown.
        filtered_frame = frame

    cv2.imshow("Filtered Frame", filtered_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()