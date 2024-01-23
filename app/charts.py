import matplotlib.pyplot as plt

def generate_bar_chart():
  labels = ['a', 'b', 'c']
  values = [10, 200, 80]
  
  fig, ax = plt.subplot()
  ax.bar(labels, values)
  plt.show()

if __name__ == '__main__':
  generate_bar_chart()