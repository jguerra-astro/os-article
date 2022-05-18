import matplotlib.pyplot as plt 
import paths
fig,ax =plt.subplots(figsize=(10,8))
x = [0,1]
ax.plot(x,x)

plt.savefig(paths.figures/"straight_line.pdf",bbox_inches='tight')