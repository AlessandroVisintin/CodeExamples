# Generalization of 100 prisoners riddle


import random
import matplotlib.pyplot as plt


class NthPrisoners:
    
    
    def __init__(self, boxes):
        self.boxes = list(range(boxes))
    
    
    def permute(self):
        random.shuffle(self.boxes)
    
    
    def circle(self, start):
        out = [start]
        out.append(self.boxes[out[-1]])
        while not out[0] == out[-1]:
            out.append(self.boxes[out[-1]])
        return set(out)
    
    
    def find_all_circles(self):
        out = []
        numbers = set(range(len(self.boxes)))
        while numbers:
            current = numbers.pop()
            tmp = self.circle(current)
            out.append(len(tmp))
            numbers = numbers - tmp
        return out

    
    def batch_test(self, rounds=1000):
        res = {}
        for dummy in range(rounds):
            self.permute()
            tmp = sorted(self.find_all_circles())
            try:
                res[tmp[-1]] += 1
            except KeyError:
                res[tmp[-1]] = 1
        
        X, Y = list(range(len(self.boxes))), [0] * len(self.boxes)
        for i in range(len(self.boxes)):
            try:
                Y[i] = res[i] / rounds
            except KeyError:
                continue

        fig, ax = plt.subplots()    
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        
        ax.set_xlabel('Max Circuit Length')
        ax.set_ylabel('Estimated probability')
        ax.grid(visible=True, linewidth=0.75, linestyle='--', c=(.9,.9,.9))
        
        plt.savefig('estimated_probability.png', dpi=300, bbox_inches='tight')
        plt.plot(X,Y)
        
        return res
        


if __name__ == '__main__':
    
    g = NthPrisoners(100)
    
    print(g.batch_test(rounds=100000))
                
        
    