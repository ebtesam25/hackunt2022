import { View, Text, Image} from "react-native";
import { Divider } from "react-native-material-ui";
import { Appbar } from "react-native-paper";
import { Icon } from 'react-native-elements';
import { theme } from "../utils/theme";
import Navbar from "../components/navbar";
import { TouchableOpacity } from "react-native";
import { useNavigation } from "@react-navigation/native";
import ProgressCircle from 'react-native-progress-circle'
import { useState } from "react";


export default function Scores () {
    const navigation = useNavigation();
    const _navigateTo = (loc) => {
        if(loc=="Transportation")[
            navigation.navigate('SelectSub')
        ]
    }

    const _getDrivingHabits = () => {
        var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "action": "getuserdrivescore",
  "userid": "3"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://us-central1-aiot-fit-xlab.cloudfunctions.net/greenscore", requestOptions)
  .then(response => response.json())
  .then(result => {console.log(result);})
  .catch(error => console.log('error', error));
    }

    const [score, setscore] = useState('')
    const [driving, setdriving] = useState('')
    const [dhabits, setdhabits] = useState({"scores": [{"score": 87, "miles": 20, "hardaccel": 2, "hardbrake": 1, "parking": 0, "avspeed": 58, "maxspeed": 82}]})
    //1 for water, 2 for food, 3 for drinks, 4 for tobacco, 5 for vehicles, 6 for general merch, 7 for energy
    const types =[{icon:"airplane", title:"Transportation"},{icon:"fast-food", title:"Food"},{icon:"ios-wine", title:"Drinks"},
    {icon:"ios-logo-no-smoking", title:"Tobacco"},{icon:"card", title:"General"},{icon:"flash", title:"Energy"}]
    return(
        <View style={{flex:1}}>
            <Text style={{textAlign:'center', fontWeight:'bold', paddingTop:'10%', paddingBottom:'5%', fontSize:17}}>Scores</Text>
            <Divider/>


            <View style={{paddingHorizontal:'5%', paddingVertical:'5%'}}>

                <View style={{flexDirection:'row', justifyContent:'space-evenly'}}><ProgressCircle
                    percent={30}
                    radius={50}
                    borderWidth={8}
                    color={theme.primary}
                    shadowColor="#999"
                    bgColor="#fff"
                >
                    <Text style={{ fontSize: 12, fontWeight:'bold' }}>Driving Score</Text>
                    <Text style={{ fontSize: 20, fontWeight:'bold' }}>{score}</Text>
                </ProgressCircle>
                <ProgressCircle
                    percent={30}
                    radius={50}
                    borderWidth={8}
                    color={theme.primary}
                    shadowColor="#999"
                    bgColor="#fff"
                >
                    <Text style={{ fontSize: 12, fontWeight:'bold' }}>Carbon Score</Text>
                    <Text style={{ fontSize: 20, fontWeight:'bold' }}>{score}</Text>
                </ProgressCircle></View>

                <Text style={{fontWeight:'bold', paddingTop:'10%', paddingBottom:'5%', fontSize:15, marginHorizontal:'5%'}}>Driving Habits</Text>


                {types.map((type)=>(<TouchableOpacity><View style={{alignSelf:'center', borderRadius:10, borderWidth:1, borderColor:theme.primary, padding:'2.5%', 
                backgroundColor:'#E7F3EB', flexDirection:'row', justifyContent:'space-between', 
                width:'90%', marginBottom:'2.5%'}}>
                    <Text style={{fontWeight:'200', color:'#000', marginLeft:'5%', textAlignVertical:'center'}}>{type.title}</Text>
                    <Text style={{fontWeight:'bold', color:theme.primary, marginLeft:'5%', textAlignVertical:'center'}}>{type.title}</Text>
                </View></TouchableOpacity>))}


            </View>
            <Navbar/>

        </View>
    )
}