from crontab import CronTab

# Crear objeto crontab para el usuario actual
cron = CronTab(user=True)

# Crear nueva tarea
job = cron.new(command='mkdir -p $HOME/microntab')

# Configurar para que se ejecute cada minuto

#job.setall('30 3 * * *')

job.minute.on(35)
job.hour.on(18)
job.day.on(19)
job.month.on(2)

# Guardar cambios
cron.write()

print("Tarea programada con éxito.")
