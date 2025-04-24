# AMA564 Course Project
This is a repository recording codes and contents about the course project set by `AMA564 Deep Learning` of `the Hong Kong Polytechnic University`.

## Group Members:
24071449g  `YU Qinyi`  <br>
24070208g  `MENG Xiaofan`

---

### Log
We recorded our initial ideas and searched for some articles to conduct a brief discussion on the financial fields with deep learning topic and wrote down details file in the `Log` folder.

### PINN
We replicated the content in the article "Gatta, F. Di Cola, V. S. Giampaolo, F. Piccialli, F.& Cuomo, S. (2023) Meshless methods for American option pricing through physics-informed neural networks. Engineering Analysis with Boundary Elements 151 68-82." by running the code under the `PINN` folder. For more details, you could refer to the "README.md" file in that folder.

### sample_data
In order to find the features used by each boundary condition clearly, we derived the corresponding sampled data and clarified the data related to each feature. 

### sigma
In order to test the performance of the PINNs model under high volatility conditions, we set the following σ values:
<img width="700" alt="联想截图_20250424195715" src="https://github.com/user-attachments/assets/eb8d4558-ba92-4857-8cc2-df3439eda075" />  <br>
The loss values of model training under these σ values or σ matrices as well as the corresponding loss oscillation figures of boundary conditions are all stored in the `sigma` folder.  <br>
You could use number or matrix content in the "matrix.txt file" within the `sigma` folder to modify the global variable "sigma" in the Jupyter Notebook file at the correspond sections 1D ~ 4D for testing under high volatility conditions.  <br>
<img width="568" alt="联想截图_20250424203542" src="https://github.com/user-attachments/assets/480f5be3-3f80-4a3e-8aed-29460c222f9c" />
