# Data Versioning with DVC

This repository demonstrates data versioning for machine learning workflows using [DVC](https://dvc.org/) (Data Version Control). DVC helps in tracking and versioning large data files and machine learning models alongside your code.

## Project Structure

- `main.py`: Script for data generation and processing
- `data/`: Directory containing versioned data files
  - `data.csv`: Dataset being versioned
- `data.dvc`: DVC tracking file for the data directory
- `S3/`: Remote storage directory for DVC data
- `projectflow.txt`: Workflow documentation

## Setup and Installation

1. **Clone the repository**
   ```powershell
   git clone <repository-url>
   cd data_versioning_DVC
   ```

2. **Install DVC**
   ```powershell
   pip install dvc
   ```

## Data Versioning Workflow

### Initial Setup
1. Initialize DVC in your project (already done):
   ```powershell
   dvc init
   ```

2. Track data directory with DVC:
   ```powershell
   dvc add data/
   ```

### Working with Data Versions

1. **Check Status**
   ```powershell
   dvc status
   ```

2. **Add New Data Version**
   ```powershell
   dvc add data/
   git add data.dvc
   git commit -m "Update data version"
   ```

3. **Push to Remote Storage**
   ```powershell
   dvc push
   ```

### Retrieving Data Versions

1. **Pull Latest Data**
   ```powershell
   dvc pull
   ```

2. **Switch Between Versions**
   ```powershell
   git checkout <commit-hash>
   dvc checkout
   ```

## Remote Storage

The project uses a local S3 directory for remote storage. In a production environment, you can configure cloud storage providers like:
- Amazon S3
- Google Cloud Storage
- Azure Blob Storage

## Best Practices

1. Always run `dvc add` after modifying tracked data
2. Commit `.dvc` files to Git after running `dvc add`
3. Use `dvc push` to ensure your data is backed up
4. Keep data and code versions in sync

## Contributing

1. Create a new branch for your changes
2. Make your modifications
3. Version any data changes using DVC
4. Submit a pull request

## License

[Add your license information here]