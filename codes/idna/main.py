import idna
encoded_domain = idna.encode('ドメイン.テスト')
print(encoded_domain)  # 输出: b'xn--eckwd4c7c.xn--zckzah'
print(idna.decode(encoded_domain))  # 输出: ドメイン.テスト

print(idna.encode('Königsgäßchen', uts46=True))  # 输出: b'xn--knigsgchen-b4a3dun'