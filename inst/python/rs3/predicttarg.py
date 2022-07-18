# AUTOGENERATED! DO NOT EDIT! File to edit: 03_predicttarg.ipynb (unless otherwise specified).

__all__ = ['load_target_model', 'predict_target']

# Cell
from rs3 import targetfeat
import joblib
import os

# Cell
def load_target_model(lite=False):
    """Load rule set 3 target model"""
    if lite:
        model_name = 'target_lite_model.pkl'
    else:
        model_name = 'target_model.pkl'
    model = joblib.load(os.path.join(os.path.dirname(__file__), model_name))
    return model

# Cell
def predict_target(design_df, aa_subseq_df, domain_feature_df=None,
                   conservation_feature_df=None, id_cols=None):
    """Make predictions using the Rule Set 3 target model. Note that if the protein_domain_df
    or conservation_df are not supplied, then the lite model will be used, otherwise the full model is used.

    :param design_df: DataFrame
    :param aa_subseq_df: DataFrame
    :param domain_feature_df: DataFrame
    :param id_cols: list or str
    :return: list
    """
    if (domain_feature_df is None) or (conservation_feature_df is None):
        lite = True
        domain_feature_df = None
        conservation_feature_df = None
    else:
        lite = False
    model = load_target_model(lite=lite)
    if id_cols is None:
        id_cols = ['sgRNA Context Sequence', 'Target Cut Length', 'Target Transcript', 'Orientation']
    target_feature_df, target_feature_cols = targetfeat.merge_feature_dfs(design_df,
                                                                          aa_subseq_df=aa_subseq_df,
                                                                          domain_df=domain_feature_df,
                                                                          conservation_df=conservation_feature_df,
                                                                          id_cols=id_cols)
    X_target = target_feature_df[target_feature_cols]
    predictions = model.predict(X_target)
    return predictions