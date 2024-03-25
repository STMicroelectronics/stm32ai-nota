# /*---------------------------------------------------------------------------------------------
#  * Copyright (c) 2024 STMicroelectronics.
#  * All rights reserved.
#  *
#  * This software is licensed under terms that can be found in the LICENSE file in
#  * the root directory of this software component.
#  * If no LICENSE file comes with this software, it is provided AS-IS.
#  *--------------------------------------------------------------------------------------------*/

import re
import matplotlib.pyplot as plt

def parse_logs_and_display_results(baseline_file, baseline_benchmark_file, compressed_file, compressed_benchmark_file):
    """
    Parses logs from baseline and compressed models and displays the results in a table.
    
    Args:
        baseline_file (str): Path to the baseline model log file.
        baseline_benchmark_file (str): Path to the baseline model benchmark log file.
        compressed_file (str): Path to the compressed model log file.
        compressed_benchmark_file (str): Path to the compressed model benchmark log file.
    """
    ram_activation = r'RAM Activations\s*:\s*([\d\.]+)\s*KiB'
    flash_weights = r'Flash weights\s*:\s*([\d\.]+)\s*KiB'
    inference_time = r'Inference_time\s*:\s*([\d\.]+)\s*ms'

    # Read accuracy data from baseline file
    with open(baseline_file, 'r') as f:
        baseline_data = f.read()
    # Extract accuracy data from baseline file
    baseline_accuracy = float(re.search(r'Accuracy of quantized model : (\d+\.\d+)', baseline_data).group(1))

    with open(baseline_benchmark_file, 'r') as f:
        baseline_data = f.read()

    # Extract RAM Activations, Flash Weights, and inference time from baseline file (second occurrence)
    b_ram_activation = float(re.search(ram_activation, baseline_data).group(1)) if re.search(ram_activation, baseline_data) else 'N/A'
    b_flash_weights = float(re.search(flash_weights, baseline_data).group(1)) if re.search(flash_weights, baseline_data) else 'N/A'
    b_inference_time = float(re.search(inference_time, baseline_data).group(1)) if re.search(inference_time, baseline_data) else 'N/A'

    # Read accuracy data from compressed file
    with open(compressed_file, 'r') as f:
        compressed_data = f.read()
    compressed_accuracy = float(re.search(r'Accuracy of quantized model : (\d+\.\d+)', compressed_data).group(1))

    with open(compressed_benchmark_file, 'r') as f:
        compressed_data = f.read()

    compressed_ram_activation = float(re.search(ram_activation, compressed_data).group(1)) if re.search(ram_activation, compressed_data) else 'N/A'
    compressed_flash_weights = float(re.search(flash_weights, compressed_data).group(1)) if re.search(flash_weights, compressed_data) else 'N/A'
    compressed_inference_time = float(re.search(inference_time, compressed_data).group(1)) if re.search(inference_time, compressed_data) else 'N/A'

    # Print the table header
    print('{:<30} {:<30} {:<30}'.format('Metric', 'Baseline Model', 'Compressed Model'))
    print('-' * 80)

    # Print the accuracy row
    print('{:<30} {:<30} {:<30}'.format('Accuracy (%)', baseline_accuracy, compressed_accuracy))

    # Print the RAM Activations row
    print('{:<30} {:<30} {:<30}'.format('RAM Activations (KiB)', b_ram_activation, compressed_ram_activation))

    # Print the Flash Weights row
    print('{:<30} {:<30} {:<30}'.format('Flash Weights (KiB)', b_flash_weights, compressed_flash_weights))

    # Print the inference time row
    print('{:<30} {:<30} {:<30}'.format('Inference time (ms)', b_inference_time, compressed_inference_time))



def generate_graphs(accuracy_baseline, accuracy_pruned, ram_baseline, ram_pruned, flash_baseline, flash_pruned, inference_time_baseline, inference_time_pruned):
    """
    Generates a comparison graph of the baseline and pruned MobileNetV2_0.35_224 models on the Flower dataset.
    The graph compares the accuracy, RAM usage, flash usage, and inference time of the two models.
    
    args:
    accuracy_baseline (float): The accuracy of the baseline model.
    accuracy_pruned (float): The accuracy of the pruned model.
    ram_baseline (float): The RAM usage of the baseline model in KiB.
    ram_pruned (float): The RAM usage of the pruned model in KiB.
    flash_baseline (float): The flash usage of the baseline model in KiB.
    flash_pruned (float): The flash usage of the pruned model in KiB.
    inference_time_baseline (float): The inference time of the baseline model in ms.
    inference_time_pruned (float): The inference time of the pruned model in ms.

    """
    # Set the figure size and spacing between subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), gridspec_kw={'wspace': 0.3, 'hspace': 0.4})
    
    # Graph 1: Accuracy Comparison
    axs[0, 0].bar(['Baseline', 'Pruned'], [accuracy_baseline, accuracy_pruned], color='#03234B')
    axs[0, 0].set_title('Accuracy')
    axs[0, 0].set_xlabel('Model')
    axs[0, 0].set_ylabel('Accuracy (%)')
    axs[0, 0].set_ylim([0, 100])
    axs[0, 0].text(0, accuracy_baseline+1, str(round(accuracy_baseline, 2))+'%')
    axs[0, 0].text(1, accuracy_pruned+1, str(round(accuracy_pruned, 2))+'%')
    
    # Graph 2: RAM Activation Comparison
    axs[0, 1].bar(['Baseline', 'Pruned'], [ram_baseline, ram_pruned], color='#03234B')
    axs[0, 1].set_title('RAM activation')
    axs[0, 1].set_xlabel('Model')
    axs[0, 1].set_ylabel('RAM activation (KiB)')
    axs[0, 1].set_ylim([0, 800])
    axs[0, 1].text(0, ram_baseline+20, str(round(ram_baseline, 2))+' KiB')
    axs[0, 1].text(1, ram_pruned+20, str(round(ram_pruned, 2))+' KiB')
    
    # Graph 3: Flash Weights Comparison
    axs[1, 0].bar(['Baseline', 'Pruned'], [flash_baseline, flash_pruned], color='#03234B')
    axs[1, 0].set_title('Flash Weights')
    axs[1, 0].set_xlabel('Model')
    axs[1, 0].set_ylabel('Flash Weights (KiB)')
    axs[1, 0].set_ylim([0, 500])
    axs[1, 0].text(0, flash_baseline+20, str(round(flash_baseline, 2))+' KiB')
    axs[1, 0].text(1, flash_pruned+20, str(round(flash_pruned, 2))+' KiB')
    
    # Graph 4: Inference Time Comparison
    axs[1, 1].bar(['Baseline', 'Pruned'], [inference_time_baseline, inference_time_pruned], color='#03234B')
    axs[1, 1].set_title('Inference Time')
    axs[1, 1].set_xlabel('Model')
    axs[1, 1].set_ylabel('Inference Time (ms)')
    axs[1, 1].set_ylim([0, 500])
    axs[1, 1].text(0, inference_time_baseline+20, str(round(inference_time_baseline, 2))+' ms')
    axs[1, 1].text(1, inference_time_pruned+20, str(round(inference_time_pruned, 2))+' ms')
    
    # Set the global title
    fig.suptitle('Comparison of Baseline and Pruned MobileNetV2_0.35_224 on Flower Dataset', fontsize=14)
    
    plt.tight_layout()
    
    # Save the figure to a file
    plt.savefig('image_classification/experiments_outputs/comparison.png')
    
    plt.show()