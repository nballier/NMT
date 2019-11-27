import pandas as pd
import matplotlib.pyplot as plt
import argparse

def create_plot(input_files,output_file,legends):
    if(len(input_files) == len(legends)):
        ax = plt.gca()
        ax.set_ylim(0,25)
        ax.set_xlim(0,160000)
        for i in range(len(input_files)):
            data = pd.read_csv(input_files[i],sep= " ", header = None)
            data.columns = ["Iterations","BLEU Score"]
            data.plot(kind='line',x='Iterations',y='BLEU Score',ax=ax)
            ax.set_ylabel("BLEU Score")
            ax.set_xlabel("Iterations")
        ax.legend(legends)
        plt.savefig(output_file)
    elif(len(input_files) > len(legends)):
        print("You forgot to add {} parameter after the -l argument, don't forget to add as much input parameters that you have legends !".format(len(input_files)-len(legends)))
    else:
        print("You forgot to add {} parameter after the -i argument, don't forget to add as much input parameters that you have legends !".format(len(legends)-len(input_files)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",nargs='+')
    parser.add_argument("-o","--output")
    parser.add_argument("-l","--legend",nargs='+')    
    args = parser.parse_args()
    create_plot(args.input,args.output,args.legend)