import torch
from opacus import PrivacyEngine

def make_private(model, optimizer, train_loader, noise_multiplier=1.0, max_grad_norm=1.0):
    """
    Wraps the PyTorch model, optimizer, and data loader with Opacus PrivacyEngine
    to enable Differentially Private SGD (DP-SGD) for hospital clients.
    """
    privacy_engine = PrivacyEngine()
    
    model, optimizer, train_loader = privacy_engine.make_private(
        module=model,
        optimizer=optimizer,
        data_loader=train_loader,
        noise_multiplier=noise_multiplier,
        max_grad_norm=max_grad_norm,
    )
    
    return model, optimizer, train_loader, privacy_engine

def get_privacy_spent(privacy_engine, delta=1e-5):
    """
    Calculates the current cumulative privacy budget expenditure (epsilon).
    """
    epsilon = privacy_engine.get_epsilon(delta)
    return epsilon, delta