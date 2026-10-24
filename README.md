# Construction Safety Compliance CV System

An AI-powered computer vision system for construction-site safety monitoring.  
The system uses YOLOv8 object detection to identify PPE items, workers, construction objects, safety violations, fall events, and zone-based risks. It also includes rule-based compliance checking, risk scoring, reporting, sample visualization, and a Streamlit dashboard.

---

## Overview

Construction sites require continuous safety monitoring to reduce accidents and improve worker compliance with personal protective equipment requirements.

This project provides a complete computer vision prototype that can detect safety-related objects and violations, analyze risk levels, generate reports, and display results through an interactive dashboard.

The system is designed as a formal portfolio-level AI project using Python, YOLOv8, OpenCV, Streamlit, and rule-based safety logic.

---

## Main Features

- PPE and construction-object detection using YOLOv8.
- Detection of hardhats, safety vests, masks, gloves, goggles, ladders, people, safety cones, and fall events.
- Rule-based PPE compliance checking.
- Risk scoring for detected safety violations.
- Critical emergency handling for fall-detection events.
- Worker tracking support.
- Zone-based safety checking.
- Image prediction support.
- Camera snapshot support.
- Video upload processing.
- Live camera dashboard mode.
- Sample prediction visualization.
- Daily safety report generation.
- GPU preflight checks before training.
- Healthcheck script for validating project readiness.
- Reasonable-time YOLO training script with auto batch, AMP, checkpoint saving, and resume support.

---

## Project Structure

```text
construction-safety-compliance-cv-system/
│
├── app/
│   └── streamlit_app.py
│
├── assets/
│   ├── sample_images/
│   └── sample_predictions/
│
├── configs/
│   ├── ppe_yolov8.yaml
│   ├── risk_rules.yaml
│   └── zones.example.json
│
├── models/
│   └── ppe_yolov8n_100e_reasonable_best.pt
│
├── scripts/
│   ├── check_dataset.py
│   ├── check_env.py
│   ├── check_training_progress.sh
│   ├── create_sample_predictions.py
│   ├── diagnose_website.py
│   ├── final_pre_training_repair.sh
│   ├── generate_daily_report.py
│   ├── gpu_preflight.py
│   ├── project_healthcheck.py
│   ├── regenerate_visible_samples.py
│   ├── run_website.sh
│   ├── train_reasonable_gpu.sh
│   └── train_strong_yolov8.sh
│
├── src/
│   ├── compliance_rules.py
│   ├── contextual_risk.py
│   ├── detection.py
│   ├── evaluate.py
│   ├── fall_alerts.py
│   ├── predict.py
│   ├── realtime.py
│   ├── reporting.py
│   ├── risk_scoring.py
│   ├── train.py
│   ├── utils.py
│   ├── video_processor.py
│   ├── visualization.py
│   ├── worker_tracking.py
│   └── zone_safety.py
│
├── tests/
│   ├── test_compliance_rules.py
│   ├── test_contextual_risk.py
│   ├── test_risk_scoring.py
│   └── test_zone_safety.py
│
├── .streamlit/
│   └── config.toml
│
├── README.md
├── TRAINING_SUMMARY.md
├── requirements.txt
└── .gitignore
```

---

## Dataset

The project expects a YOLOv8-format dataset.

Expected dataset path:

```text
/workspace/Personal Protective Equipment - Combined Model.v1i.yolov8
```

YOLO dataset configuration file:

```text
configs/ppe_yolov8.yaml
```

Dataset splits used during training:

| Split | Images |
|---|---:|
| Train | 30,765 |
| Validation | 8,814 |
| Test | 4,423 |

Number of classes:

```text
14
```

---

## Detection Classes

```text
0  Fall-Detected
1  Gloves
2  Goggles
3  Hardhat
4  Ladder
5  Mask
6  NO-Gloves
7  NO-Goggles
8  NO-Hardhat
9  NO-Mask
10 NO-Safety Vest
11 Person
12 Safety Cone
13 Safety Vest
```

---

## Final Trained Model

A lightweight trained YOLOv8n model is included for demo usage:

```text
models/ppe_yolov8n_100e_reasonable_best.pt
```

The original local training output path was:

```text
runs/train/ppe_yolov8n_100e_reasonable/weights/best.pt
```

---

## Training Configuration

The final model was trained using the following setup:

| Setting | Value |
|---|---|
| Model | YOLOv8n |
| Image size | 512 |
| Epochs | 100 |
| Batch | Auto batch |
| Device | NVIDIA GeForce RTX 3070 Ti Laptop GPU |
| AMP | Enabled |
| Cache | Disk |
| Resume support | Enabled |
| Checkpoint saving | Enabled |

Training command:

```bash
bash scripts/train_reasonable_gpu.sh 0
```

If training is interrupted, run the same command again. The script will resume from `last.pt` when available.

---

## Evaluation Results

### Validation Set

| Metric | Value |
|---|---:|
| mAP50 | 0.7664 |
| mAP50-95 | 0.4949 |
| mAP75 | 0.5273 |

### Test Set

| Metric | Value |
|---|---:|
| mAP50 | 0.7763 |
| mAP50-95 | 0.4993 |
| mAP75 | 0.5262 |

---

## Class-Level Notes

The model performs well on several important safety-related classes, including:

- Fall-Detected
- Gloves
- Goggles
- Hardhat
- Ladder
- Person
- NO-Goggles
- NO-Gloves
- NO-Hardhat

The weakest class is:

```text
NO-Safety Vest
```

This class can be improved in future work using better class balancing, additional targeted samples, or a stronger model version.

---

## Pre-Training Check

Before training, run:

```bash
python scripts/gpu_preflight.py --require-gpu --matmul
python scripts/project_healthcheck.py
```

Expected successful output:

```text
GPU status: READY
Dataset status: OK
Project healthcheck passed
```

---

## Running the Streamlit Dashboard

Start the dashboard:

```bash
bash scripts/run_website.sh
```

Open:

```text
http://localhost:8501
```

The dashboard supports:

- Image analysis
- Camera snapshot analysis
- Video upload analysis
- Live camera mode
- Sample prediction viewing
- Safety report viewing

---

## Running Evaluation

Evaluate on the validation set:

```bash
python src/evaluate.py \
  --weights models/ppe_yolov8n_100e_reasonable_best.pt \
  --split val
```

Evaluate on the test set:

```bash
python src/evaluate.py \
  --weights models/ppe_yolov8n_100e_reasonable_best.pt \
  --split test
```

---

## Regenerating Sample Predictions

```bash
python scripts/regenerate_visible_samples.py \
  --weights models/ppe_yolov8n_100e_reasonable_best.pt \
  --num-samples 12 \
  --conf 0.25 \
  --device 0
```

Generated samples are saved in:

```text
assets/sample_predictions/
```

---

## Project Healthcheck

Run the full project healthcheck:

```bash
python scripts/project_healthcheck.py
```

This checks:

- Required project files
- Python package availability
- Python syntax compilation
- Dataset structure
- Test suite

---

## Testing

Run tests:

```bash
pytest
```

The current test suite covers:

- Compliance rules
- Risk scoring
- Contextual risk logic
- Zone safety logic

---

## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Core dependencies include:

- Python
- PyTorch
- Ultralytics YOLO
- OpenCV
- Streamlit
- Pandas
- PyYAML
- Pillow
- Matplotlib
- Pytest

---

## Safety Disclaimer

This system is a safety-assistance prototype.  
It supports visual inspection, safety monitoring, and reporting, but it does not replace official site supervision, certified safety procedures, or professional safety officers.

---

## Future Improvements

Possible future improvements include:

- Stronger model training using YOLOv8s or YOLOv8m.
- Better class balancing for weak classes such as `NO-Safety Vest`.
- More construction-site data from different lighting and camera angles.
- Improved worker re-identification.
- More advanced fall-event confirmation logic.
- FastAPI backend integration.
- Docker deployment.
- Database storage for historical reports.
- Real-time alert notifications.
- Role-based dashboard access.

---

## Repository Status

This repository includes:

- Clean project structure.
- Trained YOLOv8n model.
- Streamlit dashboard.
- Safety compliance logic.
- Risk scoring logic.
- Worker tracking and zone safety modules.
- Training and evaluation scripts.
- Sample prediction outputs.
- Project healthcheck and tests.

```text
Status: GitHub-ready portfolio project
```
