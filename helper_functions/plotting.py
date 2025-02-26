# helper_functions/plotting.py
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

def plot_param_trait(effect, trait, data_frame, *export_path_fig):
    plt.figure(figsize=(6,4))
    if effect in ["volatility", "noise"]:
        col_1, col_2 = f"{effect}_effect_high_noise", f"{effect}_effect_low_noise"
    else:
        raise ValueError("Unknown effect type")
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,5))
    index = 0
    for i, ax in enumerate(axes.flatten()):
        if index == 0:
            sns.regplot(x = trait, y = col_1, data = data_frame, ax = ax)
            spearman = stats.spearmanr(data_frame[trait], data_frame[col_1])
            corr_text = "spearmanr = {:.3f}, p = {:.3f}".format(spearman.correlation, spearman.pvalue)
            ax.title.set_text("Relationship bewteen " + trait + " and " + col_1 + "\n" + corr_text)
        else:
            sns.regplot(x = trait, y = col_2, data = data_frame, ax = ax)
            spearman = stats.spearmanr(data_frame[trait], data_frame[col_2])
            corr_text = "spearmanr = {:.3f}, p = {:.3f}".format(spearman.correlation, spearman.pvalue)
            ax.title.set_text("Relationship bewteen " + trait + " and " + col_2 + "\n" + corr_text)
        index = index + 1
    fig.tight_layout()
    if export_path_fig:
        plt.show()
        plt.savefig(export_path_fig[0] + effect + " " + trait +".png", transparent = True, dpi = 300)
    else:
        plt.show()
        # plt.savefig(export_path_fig + effect + " " + trait +".png", transparent = True, dpi = 300)
    plt.show()
    return ""

def plot_block_trait(trait, outcome_var, data_frame):
    plt.clf()
    plot_order = ["Highbias_LowNoise", "Highbias_HighNoise", "Lowbias_LowNoise", "Lowbias_HighNoise"]
    g = sns.lmplot(data = data_frame, x= trait, y=outcome_var, col="block", col_order = plot_order, sharey=False, height=3,aspect=1.2)
    g.set_axis_labels(trait, outcome_var)
    
    axes = g.axes.flatten()
    i = 0
    while i < 4:
        df_stats = data_frame[data_frame.block == plot_order[i]]
        spearman = stats.spearmanr(df_stats[trait], df_stats[outcome_var])
        corr_text = "spearmanr = {:.3f}, p = {:.3f}".format(spearman.correlation, spearman.pvalue)
        axes[i].set_title(trait + " and " + "\n" + outcome_var + "\n" + " in " + plot_order[i] + "\n" + corr_text)
        i = i + 1
        
    plt.tight_layout()
    
    
    if export_path_fig:
        plt.subplots_adjust(top=0.9)
        plt.show()
        plt.savefig(export_path_fig[0] + outcome_var + " " + trait +".png", transparent = True, dpi = 300)
    else:
        plt.subplots_adjust(top=0.9)
        plt.show()
        #plt.savefig(export_path_fig + effect + " " + trait +".png", transparent = True, dpi = 300)
        
    plt.subplots_adjust(top=0.9)
    plt.show()
    return ""

def plot_alpha_beta_project3_param_trait(effect, variable, trait, data_frame):
    plt.figure(figsize=(6,4))
    if (effect == "bias") and (variable in ["alpha", "beta"]):
        col_1, col_2 = f"bias_effect_high_noise", f"bias_effect_low_noise"
    elif (effect == "noise") and (variable in ["alpha", "beta"]):
        col_1, col_2 = f"noise_effect_high_bias", f"noise_effect_low_bias"
    else:
        raise ValueError("Unknown effect or variable type")
    sns.regplot(x=trait, y=col_1, data=data_frame)
    sns.regplot(x=trait, y=col_2, data=data_frame)
    plt.xlabel(trait)
    plt.ylabel(effect)
    plt.title(f"{effect} ({variable}) vs {trait}")
    plt.show()
    
def plot_model3_project3_param_trait (effect, variable, trait, data_frame, *export_path_fig):
    plt.clf()
    if (effect == "bias") & (variable == "lr_theta"):
        col_1 = 'bias_effect_high_noise'
        col_2 = 'bias_effect_low_noise'
    if (effect == "noise" ) & (variable == "lr_theta"):
        col_1 = 'noise_effect_high_bias'
        col_2 = 'noise_effect_low_bias'
    if (effect == "bias") & (variable == "lr_change"):
        col_1 = 'change_bias_effect_high_noise'
        col_2 = 'change_bias_effect_low_noise'
    if (effect == "noise" ) & (variable == "lr_change"):
        col_1 = 'change_noise_effect_high_bias'
        col_2 = 'change_noise_effect_low_bias'
    if (effect == "bias") & (variable == "sensitivity"):
        col_1 = 'sensitivity_bias_effect_high_noise'
        col_2 = 'sensitivity_bias_effect_low_noise'
    if (effect == "noise" ) & (variable == "sensitivity"):
        col_1 = 'sensitivity_noise_effect_high_bias'
        col_2 = 'sensitivity_noise_effect_low_bias'
    if (effect == "bias") & (variable == "mixture"):
        col_1 = 'mixture_bias_effect_high_noise'
        col_2 = 'mixture_bias_effect_low_noise'
    if (effect == "noise" ) & (variable == "mixture"):
        col_1 = 'mixture_noise_effect_high_bias'
        col_2 = 'mixture_noise_effect_low_bias'
    if (effect == "bias") & (variable == "prec"):
        col_1 = 'prec_bias_effect_high_noise'
        col_2 = 'prec_bias_effect_low_noise'
    if (effect == "noise" ) & (variable == "prec"):
        col_1 = 'prec_noise_effect_high_bias'
        col_2 = 'prec_noise_effect_low_bias'
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,5))
    index = 0
    for i, ax in enumerate(axes.flatten()):
        if index == 0:
            sns.regplot(data = data_frame, x = trait, y = col_1, ax = ax)
            spearman = stats.spearmanr(data_frame[trait], data_frame[col_1])
            corr_text = "spearmanr = {:.3f}, p = {:.3f}".format(spearman.correlation, spearman.pvalue)
            ax.title.set_text("Relationship bewteen " + trait + " and " + col_1 + "\n" + corr_text)
        else:
            sns.regplot(data = data_frame, x = trait, y = col_2, ax = ax)
            spearman = stats.spearmanr(data_frame[trait], data_frame[col_2])
            corr_text = "spearmanr = {:.3f}, p = {:.3f}".format(spearman.correlation, spearman.pvalue)
            ax.title.set_text("Relationship bewteen " + trait + " and " + col_2 + "\n" + corr_text)
        index = index + 1
    fig.tight_layout()
    # plt.savefig(export_path_fig[0] + effect +"_"+ "model3" + "_" + trait +".png", transparent = True, dpi = 300)

    plt.show()
    return ""

