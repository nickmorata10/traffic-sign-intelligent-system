echo "Running system..."

python src/data_pipeline.py
python src/train.py
python src/eval.py

echo "Finished"
