// coding: utf-8
// @Author : lryself
// @Date : 2022/1/18 10:57
// @Software: GoLand

package http1

import (
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
)

func interfaceToMap(m interface{}) map[string]interface{} {
	return m.(map[string]interface{})
}

func HttpGetServer(reqUrl string) ([]byte, error) {
	resp, err := http.Get(reqUrl)
	if err != nil {
		return nil, err
	}
	body, err := ioutil.ReadAll(resp.Body)
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		return nil, errors.New(fmt.Sprintf("请求出错，状态码：%d", err))
	}
	return body, nil
}
