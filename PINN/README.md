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
The original 'requirements.txt' cannot support the IDE of the whole code. We changed the versions of several packages and exported all of the needed packages to conda_forge_requirement.txt, pip_requirements.txt and other_requirements.txt in the `Requirements` folder. You could download the environment by running the following commands by order:

`
conda create -n PINN python=3.9
`
\
`
conda install --file conda_forge_requirements.txt -c conda-forge
`
\
`
pip install -r pip_requirements.txt
`
\
`
conda install --file other_requirements.txt
`

Since some functions require a specific tensorflow framework version, you will need to update tensorflow with the following command:

`
pip install tensorflow==2.8.0
`

---

### Network
The figures in the `Network` folder illustrate the network structures utilized by the PINNs model, where solution network employs n-dimensional underlying asset price _S_ and time _t_ to obtain forecast option price _P(S, t)_ while free boundary network uses time _t_ to get n-dimensional "sufficiently low price" _B(t)_.

### losses_tables&figures
We set the variable "random_seed" to 10 prime numbers to run the code for the 1D to 4D sections of the "PINN_4_AmericanOptions.ipynb" file and saved the generated loss values of related boundary conditions and the corresponding loss figures to the subdirectories 1D ~ 4D in the `losses_tables&figures` folder.
