# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: agouet <agouet@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/26 09:54:13 by agouet            #+#    #+#              #
#    Updated: 2023/10/26 13:19:55 by agouet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
import time


dt = datetime.date.today()

# sec since Unix Epoch
t_unix = time.time()

print(f"Seconds since January 1, 1970: {t_unix:,.4f} or {t_unix:.2e} in scientific notation")
print(dt.strftime("%b"), dt.day, dt.year)
