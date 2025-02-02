import torch
import torch.nn as nn

class WebsiteModel(nn.Module):
    def __init__(self):
        super(WebsiteModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, stride=1, padding=1)
        self.fc1 = nn.Linear(16 * 28 * 28, 2)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = x.view(x.size(0), -1)
        return self.fc1(x)

    def predict(self, image_tensor):
        with torch.no_grad():
            output = self.forward(image_tensor)
            return torch.argmax(output, dim=1).item()
