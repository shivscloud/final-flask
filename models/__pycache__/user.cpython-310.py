o
    _�dq  �                   @   s   d dl mZ G dd� d�ZdS )�    )�connc                   @   s4   e Zd Zdd� Zdd� Zedd� �Zedd� �Zd	S )
�Userc                 C   s
   || _ d S )N)�username)�selfr   � r   �D:\mainpy\models\user.py�__init__   s   
zUser.__init__c                 C   s$   t �� }|�d| jf� t ��  d S )Nz(INSERT INTO users (username) VALUES (%s))r   �cursor�executer   �commit)r   r	   r   r   r   �save   s   z	User.savec                  C   s   t �� } | �d� | �� }|S )NzSELECT * FROM users)r   r	   r
   Zfetchall)r	   �usersr   r   r   �get_all   s   
zUser.get_allc                 C   s"   t �� }|�d| f� t ��  d S )NzDELETE FROM users WHERE id = %s)r   r	   r
   r   )�user_idr	   r   r   r   �delete   s   zUser.deleteN)�__name__�
__module__�__qualname__r   r   �staticmethodr   r   r   r   r   r   r      s    
r   N)r   r   r   r   r   r   r   �<module>   s    