# 100 = 65535
# 1 = 655.35

VOLUME_UNIT = 655.35

def convert_human_to_nir_values(human_volume_value):
  
  """
  Converts human friendly volume values to Nircmd compatable values
  Arguments:
  [int] human_volume_value

  Returns:
  [float] nircmd_friendly_volume 
  """
  return VOLUME_UNIT * human_volume_value