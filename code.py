import matplotlib.pyplot as plt

# -----------------------------
# Academic Data
# -----------------------------
semesters = [1, 2, 3, 4, 5]
semester_gpa = [8.5, 8.2, 7.9, 8.9, 7.9]

# -----------------------------
# Compute CGPA
# -----------------------------
cgpa = []
cumulative_sum = 0

for i, gpa in enumerate(semester_gpa):
    cumulative_sum += gpa
    cgpa.append(round(cumulative_sum / (i + 1), 2))

# -----------------------------
# Plot Configuration
# -----------------------------
plt.figure(figsize=(9, 5))

plt.plot(
    semesters,
    semester_gpa,
    marker='o',
    linewidth=2,
    label='Semester GPA'
)

plt.plot(
    semesters,
    cgpa,
    marker='s',
    linestyle='--',
    linewidth=2,
    label='CGPA'
)

# -----------------------------
# Labels & Title
# -----------------------------
plt.xlabel("Semester")
plt.ylabel("GPA")
plt.xticks(semesters)
plt.ylim(7.5, 9.2)

plt.title(
    "Semester-wise Academic Performance\n"
    "Rajiv Gandhi University of Knowledge Technologies\n"
    "B.Tech in Computer Science and Engineering",
    fontsize=12
)

# -----------------------------
# Annotations (Data Storytelling)
# -----------------------------
plt.annotate(
    "Performance dip & recovery",
    xy=(3, 7.9),
    xytext=(2.2, 8.9),
    arrowprops=dict(arrowstyle="->")
)

plt.annotate(
    "Peak academic performance",
    xy=(4, 8.9),
    xytext=(4.2, 8.3),
    arrowprops=dict(arrowstyle="->")
)

# -----------------------------
# Styling
# -----------------------------
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# -----------------------------
# Save Figure
# -----------------------------
plt.savefig("semester_gpa_cgpa_plot.png", dpi=200)
plt.show()
