from tflite_support.metadata_writers import writer_utils
from tflite_support.metadata_writers import image_classifier
from tflite_support.metadata_writers import metadata_info

# Path ke model TFLite
model_path = 'model.tflite'
label_file_path = 'labels.txt'

# Buat file label
labels = [
    'battery', 'biological', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash'
]
with open(label_file_path, 'w') as f:
    for label in labels:
        f.write(f"{label}\n")

# Memuat model dan membuat metadata writer
model_buffer = writer_utils.load_file(model_path)
writer = image_classifier.MetadataWriter.create_for_inference(
    model_buffer,
    input_norm_mean=[127.5],  # mean normalization
    input_norm_std=[127.5],   # std normalization
    label_file_paths=[label_file_path]
)

# Tempat penyimpanan model dengan metadata
tflite_with_metadata_path = 'model_with_metadata.tflite'
writer_utils.save_file(writer.populate(), tflite_with_metadata_path)

print(f"Metadata has been written to {tflite_with_metadata_path}")
