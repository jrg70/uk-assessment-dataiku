# run.py
import yaml
from data import load_data
from preprocess import preprocess_data

# --- Load config file ---
with open("config/config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

TRAIN = f"{cfg['paths']['raw']}/census_income_learn.csv"
TEST  = f"{cfg['paths']['raw']}/census_income_test.csv"
TARGET = cfg["target"]  # dynamically load target column name

def main():
    # Load data
    train_df, test_df = load_data(TRAIN, TEST)
    print("Loaded:", train_df.shape, test_df.shape)

    # Preprocess data
    train_clean = preprocess_data(train_df, target_col=TARGET)
    test_clean  = preprocess_data(test_df, target_col=TARGET)
    print("Cleaned:", train_clean.shape, test_clean.shape)

    # Save processed files
    train_clean.to_csv(f"{cfg['paths']['processed']}/train_clean.csv", index=False)
    test_clean.to_csv(f"{cfg['paths']['processed']}/test_clean.csv", index=False)
    print("Saved cleaned files")

if __name__ == "__main__":
    main()
