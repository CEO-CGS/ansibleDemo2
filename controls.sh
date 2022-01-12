
#call our inventory myhosts, with one group called group1
echo "[group1]" > myhosts

#add host to myhosts
echo "host01 ansible_ssh_user=ubuntu" >> myhosts

#run playbook with inventory with -i
ansible-playbook -i myhosts site.yml
