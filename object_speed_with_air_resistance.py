import numpy as np
import matplotlib.pyplot as plt
import rocket_draw as rd

# speed graphic for sphere with air resistance

# delta V parameters
P = 10             # Total rocket impulse
t_engine = 1.86                # time that engine works
thrust_force = P / t_engine
Mt = 0.010           # Mass of fuel
m0 = 0.0396            # start rocket mass
m1 = m0 - Mt
g = 9.81      # gravity acceleration


Py = P / (Mt * g)             # Specific impulse
v_delta = Py * np.log(m0 / m1) # delta v

# air resistance parameters
Cf = 0.1      # resistance coefficient
p = 1.225     # air density
S = 0.0019     # cross sectional area m
# Integration parameters
t0 = 0.0      # start graph time
t_max = 20.0  # end graph time
h = 0.1      # integration step, s

def thrust(t):
    if t <= t_engine:
        return thrust_force
    else:
        return 0

def f(t, v):
    engine_force = thrust(t)
    return (engine_force - m0 * g - (0.5 * Cf * p * S * v**2)) / m0

# Метод Рунге-Кутты 4-го порядка
def runge_kutta_4(v0, t0, t_max, h):
    t_values = np.arange(t0, t_max, h)
    v_values = []
    t_iterations = 0
    v = v0
    for t in t_values:
        k1 = f(t, v)
        k2 = f(t + h / 2, v + h / 2 * k1)
        k3 = f(t + h / 2, v + h / 2 * k2)
        k4 = f(t + h, v + h * k3)

        v = v + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        if v < 0:
            break
        t_iterations += 1
        v_values.append(v)

    new_t_values = np.zeros(t_iterations)
    new_t_values = t_values[0:t_iterations]
    return new_t_values, v_values

t_values, v_values = runge_kutta_4(0, t0, t_max, h)

t_values = np.array(t_values)
v_values = np.array(v_values)

dt = np.diff(t_values)
average_velocity = (v_values[:-1] + v_values[1:]) / 2
s_values = np.cumsum(dt * average_velocity)

s_values = np.insert(s_values, 0, 0)


# Plot and show animation
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(t_values, v_values, label="Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t_values, s_values, label="Distance", color="green")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.title("Distance vs Time")
plt.grid(True)
plt.legend()
# show graphics
plt.tight_layout()
plt.show()


# Matpotlib window setup
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ion()

attitude = 0
translation = np.array([0, 0, 0])

# objectHigh koef
k = max(s_values) / 50
print("Begin animation")
for i in s_values:
    attitude = i

    print(attitude)
    rd.setZCube(rd.cube_vertices, attitude, objectHigh=5 * int(k))

    rd.create_cube(ax, rd.cube_vertices, max(s_values))
    plt.draw()
    plt.pause(0.1)
print("End animation")
print(f"max attitude {max(s_values)}")