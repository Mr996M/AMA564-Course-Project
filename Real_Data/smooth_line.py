import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

T = [0.50, 1.00, 1.50, 2.00, 2.50, 3.00]
Free_Boundary_Loss = [0.011135, 0.008944, 0.009691, 0.006370, 0.013896, 0.024720]

x = np.array(T)
y = np.array(Free_Boundary_Loss)

degree = 3
coeffs = np.polyfit(x, y, degree)
poly_eq = np.poly1d(coeffs)
x_smooth_poly = np.linspace(x.min(), x.max(), 200)
y_smooth_poly = poly_eq(x_smooth_poly)

spl = UnivariateSpline(x, y, s=0.5)
x_smooth_spline = np.linspace(x.min(), x.max(), 200)
y_smooth_spline = spl(x_smooth_spline)

# Draw the figure
plt.figure(figsize=(10, 6))

# The original data
plt.scatter(x, y, color='red', label='Original Data', zorder=3)

# Draw the smooth line to fit
plt.plot(x_smooth_poly, y_smooth_poly, 'b--', linewidth=2,
         label=f'Polynomial Fit (degree={degree})')
plt.plot(x_smooth_spline, y_smooth_spline, 'g-', linewidth=2,
         label='Spline Fit')

plt.xlabel('T', fontsize=12)
plt.ylabel('Free Boundary Loss', fontsize=12)
plt.title('Smoothing Fitting Figure', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()