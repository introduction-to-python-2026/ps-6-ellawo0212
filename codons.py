def create_codon_dict(file_path):
  path = file_path
  file = open(path,"r")
  rows = file.readlines()
  file.close() 
  codon_dict={}
  for i in rows:
    cell= i.strip().split('\t')
    codon=cell[0]
    emino_acid=cell[2]
    codon_dict[codon]=emino_acid
  return codon_dict

