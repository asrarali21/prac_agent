from datasets import load_dataset


def load_any_dataset(name: str = "ag_news", split: str = "train", sample_size: int = 5):
    """
    Load a dataset from Hugging Face and return a small sample.
    """
    ds = load_dataset(name, split=split)
    return ds.select(range(min(sample_size, len(ds))))


if __name__ == "__main__":
    dataset_sample = load_any_dataset()
    print(dataset_sample)
    print(dataset_sample[0])