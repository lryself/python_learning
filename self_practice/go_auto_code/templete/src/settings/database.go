package settings

import (
	"{{project_name}}/src/globals"
	"{{project_name}}/src/globals/database"
	"github.com/spf13/viper"
)

var log = globals.GetLogger()

func InitDatabase() (err error) {
	if viper.GetBool("system.UseMysql") {
		err = database.InitMysqlClient()
		if err != nil {
			log.Errorln("mysql初始化出错:", err)
			return
		}
	}
	if viper.GetBool("system.UseRedis") {
		err = database.InitRedisClient()
		if err != nil {
			log.Errorln("redis初始化出错:", err)
			return
		}
	}
	return
}
