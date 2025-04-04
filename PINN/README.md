# Meshless-Methods-for-American-Option-Pricing-by-using-Physics-Informed-Neural-Networks
This repository is created to share code for American put option pricing by means of Physics Informed Neural Networks (PINN)

### News
- 2022-09-04 Repository created.
- 2022-09-11 Notebook Python uploaded

---

### Requires
The code has been developed in Google Colab. The exact requirements are contained in 'requirements.txt'.

`
pip install -r requirements.txt
`

### New environment version
The original 'requirements.txt' cannot support the IDE of the whole code. We changed the versions of several packages and exported all of the needed packages to conda_forge_requirement.txt, pip_requirements.txt and other_requirements.txt. You could download the environment by running the following commands by order:

`
conda create -n PINN python=3.9
conda install --file conda_forge_requirements.txt -c conda-forge
conda install --file other_requirements.txt
pip install -r pip_requirements.txt
`
